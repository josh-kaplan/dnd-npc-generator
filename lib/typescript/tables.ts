import { Option, WeightedValue } from "./index";
import { getGroups } from "./utils";
import path from "path";
import {promisify} from 'util';



/*--------------------( Globals )-------------------------------*/
const tables = {} as Tables;
let isInitialized = false;



/*--------------------( Private Interfaces )--------------------*/

interface TableEntry {
  w: number,
  options: Option[]
}

interface Tables {
  [name: string]: TableEntry
}


/*--------------------( Public Interfaces )---------------------*/

export interface NamedOption extends Option {
  name?: string;
}

/**
 * 
 */
export interface TableReferenceOption extends NamedOption {
  table: string;
}



/*--------------------( Private Functions )---------------------*/


/**
 *
 */
function initAvailableTables(files: string[]) {
  for (const file of files) {
    const name = path.basename(file, ".json");
    tables[name] = {w: 0, options: []};
  }
  isInitialized = true;
}

/**
 *
 */
function importTable(tableName: string, r: (id: string) => any) {
  const name = path.basename(tableName, ".json");
  const table: WeightedValue[] = r(tableName);
  let totalWeight = 0;
  const options = table.map(row => {
    const w = row.w > 0 ? row.w : 0;
    totalWeight += w;
    return {
      ...row,
      w,
      v: getGroups(row.v) || [],
      original: row.v
    }
  });
  tables[name].options = options;
  tables[name].w = totalWeight;
}

/**
 *
 */
async function ensureTablesAreInitialized() {
  if (!isInitialized) {
    const fs = require("fs");
    const glob = require("glob");
    const dir = path.join(__dirname, "./tables");
    const files = fs.readdirSync(dir).filter((f:string) => f.endsWith('.json')); //[];
    
    /*const loadTables = (cwdwd) => {
      fs.readdirSync(c).filter((f:string) => {
        f.endsWith('.json')
      });
    }
    loadTables(dir)

    console.log(files)*/

    initAvailableTables(files);
    for (const table of files) {
      importTable(table, t => require(path.join(dir, t)));
    }

    
  }
}


/*--------------------( Public Functions )----------------------*/

/**
 * 
 */
export function getTableNames() {
  ensureTablesAreInitialized();
  return Object.keys(tables);
}

/**
 * @param {string}
 */
export function getTable(tableName: string) {
  ensureTablesAreInitialized();
  if (!(tableName in tables)) {
    throw new Error(`Unable to find table [${tableName}]`);
  }
  return tables[tableName];
}

/**
 * 
 */
export function getNamedTableOptions(tableName: string): NamedOption[] {
  const options = getTable(tableName).options;
  return options as NamedOption[];
}

/**
 * @param  {string}
 * @return {TableReferenceOption[]}
 */
export function getTableReferenceOptions(tableName: string): TableReferenceOption[] {
  const options = getTable(tableName).options as any;
  for (const opt of options) {
    if (!("table" in opt)) {
      throw new Error(`Missing "table" property in table ${tableName} option ${opt.original}`);
    }
  }
  return options as TableReferenceOption[];
}

/**
 * @param {string}
 */
export function getTableWeight(tableName: string) {
  return getTable(tableName).w;
}

/**
 * @param {string}
 */
export function getTableOptions(tableName: string) {
  return getTable(tableName).options;
}
