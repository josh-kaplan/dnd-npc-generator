import { Group, Operator } from "./index";
import {getTable} from "./tables";
import * as s from "./staticAnalysis";


/*--------------------( Globals )-------------------------------*/

export const debugGen = process.env.NODE_ENV === "development";
export const reGroup = /{((\\{|\\}|[^{}])*)}|((\\{|\\}|[^{}])+)/g;


/*--------------------( Private Functions )---------------------*/


/**
 * @param  {string}
 * @return {Group}
 */
function mapGroup(g: string): Group {
  //todo: replace escaped \{ and \}
  if (g[0] === "{") {
    for (const op of operators) {
      const m = g.match(op.regex);
      if (m) {
        return op.makeOperator(m);
      }
    }
    return () => { };
  }
  return g;
}


/**
 * @param  {any}
 * @return {n}
 */
function isNumber(n: any): n is number {
  return typeof n === "number";
}


/*--------------------( Public Functions )----------------------*/


/**
 * @param {number}
 */
export function abilityWithMod(ability: number) {
    let nModifier = (ability-10)%2;
    let modifier = (nModifier >= 0) ? `+${nModifier}` : `${nModifier}`;
    let spaces = (ability < 10) ? ' ' : '';
    return `${spaces}${ability} (${modifier})`;
}

/**
 * @param {any}
 */
export function cm2ft(cm: any) {
    let _inches = 0.393701 * Number(cm);
    let ft = Math.floor(_inches/12) 
    let inch = Math.round(_inches % 12);
    return `${ft}'${inch}"`;
}


/**
 * @param {any}
 */
export function printNPC(npc: any) {
    let pronoun = npc.description.pronounCapit;
    let ft = cm2ft(npc.physical.height);

    let color = '\u001b[36m'
    let esc = '\u001b[0m'

    console.log(`
${color}Description${esc}
${npc.description.name} is a ${npc.description.age} year old ${npc.description.gender} ${npc.description.race} ${npc.description.occupation}.
${pronoun}has ${npc.physical.hair}${npc.physical.eyes}. 
${pronoun}has ${npc.physical.skin} and ${npc.physical.face}.
${pronoun}has ${npc.physical.build} and stands ${npc.physical.height}cm (${ft}) tall.
${npc.physical.special1}  ${npc.physical.special2}

${color}Personality and Background${esc}
${npc.ptraits.traits1}
${npc.ptraits.traits2}
${npc.pquirks.description}
${npc.hook.description}
${npc.religion.description}

${color}Alignment Tendencies${esc}
Good, Neutral, Evil:      ${npc.alignment.good}, ${npc.alignment.moralneutral}, ${npc.alignment.evil}
Lawful, Neutral, Chaotic: ${npc.alignment.lawful}, ${npc.alignment.ethicalneutral}, ${npc.alignment.chaotic}

${color}Stats${esc}
STR    ${abilityWithMod(npc.abilities.str)}        INT    ${abilityWithMod(npc.abilities.int)}
DEX    ${abilityWithMod(npc.abilities.dex)}        WIS    ${abilityWithMod(npc.abilities.wis)}
CON    ${abilityWithMod(npc.abilities.con)}        CHA    ${abilityWithMod(npc.abilities.cha)}
`);
}


/**
 * [w description]
 * @type {number}
 */
export function chooseRandomWithWeight<T>(arr: {
  w: number;
  v: T
}[], totalWeight: number): T {
  let rnum = ((Math.random() * totalWeight) + 1) | 0;
  let i = 0;
  while (rnum > 0) {
    rnum -= arr[i++].w;
  }
  return arr[i - 1].v;
}


/**
 * @param  {string}
 * @return {Group[]}
 */
export function getGroups(val: string): Group[] {
  if (typeof val !== "string" || val.length === 0) {
    throw new Error("Empty value to get group");
  }
  val = val.replace("{\\n}", "\n");
  const r = (val.match(reGroup) || [])
    .map(g => {
      const r = mapGroup(g);
      if (debugGen && typeof r !== "string") {
        r.original = g;
      }
      return r;
    });
  return r;
}


/*--------------------( Interpreter ) --------------------------*/


/*
All supported operations
{%v1=%v2} : v1 = v2
{%v1=15} : v1 = 15
{%v1+%v2} : v1 = v1 + v2
{%v1+15} : v1 = v1 + 15
{%v1-%v2} : v1 = v1 - v2
{%v1-15} : v1 = v1 - 15
{%v1} : output v1
{$s1=$s2} : s1 = s2
{$s1=du text lala.} : s1 = txt
{$s1+$s2} : s1 = s1 + s2
{$s1+du text lala.} : s1 = s1 + txt
{$s1} : output s1
{\n} : output an endline
{table} : replace by table element
*/
export const operators: {
  regex: RegExp,
  makeOperator: (m: RegExpMatchArray) => Operator,
  analysis: (m: RegExpMatchArray) => s.StaticAnalysis,
}[] = [
    // {%v1=%v2}
    {
      regex: /^{%(.+)=%(.*)}/, makeOperator(m) {
        const v1 = m[1], v2 = m[2];
        return function operator(context) {
          context.vars[v1] = +context.vars[v2];
        };
      },
      analysis: m => ({
        def: [new s.NumberDef(m[1])],
        use: [new s.NumberUse(m[2])]
      })
    },
    // {%v1=15}
    {
      regex: /^{%(.+)=(.*)}/, makeOperator(m) {
        const v1 = m[1], value = +m[2];
        return function operator(context) {
          context.vars[v1] = value;
        };
      },
      analysis: m => ({
        def: [new s.NumberDef(m[1])]
      })
    },
    // {%v1+%v2}
    {
      regex: /^{%(.+)\+%(.*)}/, makeOperator(m) {
        const v1 = m[1], v2 = m[2];
        return function operator(context) {
          context.vars[v1] = (+context.vars[v1]) + (+context.vars[v2]);
        };
      },
      analysis: m => ({
        def: [new s.NumberDef(m[1])],
        use: [new s.NumberUse(m[1]), new s.NumberUse(m[2])]
      })
    },
    // {%v1+15}
    {
      regex: /^{%(.+)\+(.*)}/, makeOperator(m) {
        const v1 = m[1], value = +m[2];
        return function operator(context) {
          context.vars[v1] = (+context.vars[v1]) + value;
        };
      },
      analysis: m => ({
        def: [new s.NumberDef(m[1])],
        use: [new s.NumberUse(m[1])]
      })
    },
    // {%v1-%v2}
    {
      regex: /^{%(.+)-%(.*)}/, makeOperator(m) {
        const v1 = m[1], v2 = m[2];
        return function operator(context) {
          context.vars[v1] = (+context.vars[v1]) - (+context.vars[v2]);
        };
      },
      analysis: m => ({
        def: [new s.NumberDef(m[1])],
        use: [new s.NumberUse(m[1]), new s.NumberUse(m[2])]
      })
    },
    // {%v1-15}
    {
      regex: /^{%(.+)-(.*)}/, makeOperator(m) {
        const v1 = m[1], value = +m[2];
        return function operator(context) {
          context.vars[v1] = (+context.vars[v1]) - value;
        };
      },
      analysis: m => ({
        def: [new s.NumberDef(m[1])],
        use: [new s.NumberUse(m[1])]
      })
    },
    // {%v1}
    {
      regex: /^{%(.+)}/, makeOperator(m) {
        const v1 = m[1];
        return function operator(context) {
          return (+context.vars[v1]) | 0;
        };
      },
      analysis: m => ({
        use: [new s.NumberUse(m[1])]
      })
    },
    // {$s1=$s2}
    {
      regex: /^{\$(.+)=\$(.*)}/, makeOperator(m) {
        const s1 = m[1], s2 = m[2];
        return function operator(context) {
          context.vars[s1] = String(context.vars[s2]);
        };
      },
      analysis: m => ({
        def: [new s.StringDef(m[1])],
        use: [new s.StringUse(m[2])]
      })
    },
    // {$s1=du text lala.}
    {
      regex: /^{\$(.+)=(.*)}/, makeOperator(m) {
        const s1 = m[1], text = m[2];
        return function operator(context) {
          context.vars[s1] = text;
        };
      },
      analysis: m => ({
        def: [new s.StringDef(m[1])],
      })
    },
    // {$s1+$s2}
    {
      regex: /^{\$(.+)\+\$(.*)}/, makeOperator(m) {
        const s1 = m[1], s2 = m[2];
        return function operator(context) {
          context.vars[s1] += String(context.vars[s2]);
        };
      },
      analysis: m => ({
        def: [new s.StringDef(m[1])],
        use: [new s.StringUse(m[1]), new s.StringUse(m[2])]
      })
    },
    // {$s1+du text lala.}
    {
      regex: /^{\$(.+)\+(.*)}/, makeOperator(m) {
        const s1 = m[1], text = m[2];
        return function operator(context) {
          context.vars[s1] += text;
        };
      },
      analysis: m => ({
        def: [new s.StringDef(m[1])],
        use: [new s.StringUse(m[1])]
      })
    },
    // {$s1}
    {
      regex: /^{\$(.+)}/, makeOperator(m) {
        const s1 = m[1];
        return function operator(context) {
          return context.vars[s1];
        };
      },
      analysis: m => ({
        use: [new s.StringUse(m[1])]
      })
    },
    {
      regex: /^{\\n}$/, makeOperator() {
        return function operator() {
          return "\n";
        };
      },
      analysis: m => ({})
    },
    // {table}
    {
      regex: /^{(.*)}/, makeOperator(m) {
        const tablename = m[1];
        const t = getTable(tablename);
        return function operator(context, options) {
          function chooseOption(index: number) {
            if ((index >>> 0) >= t.options.length) {
              console.warn("Index [%d] for table [%s]", index, tablename);
              return chooseRandomWithWeight(t.options, t.w);
            }
            /*if(__DEV__) {
              console.log(
                "Table [%s] option forced to [%s]",
                tablename,
                t.options[index].original
              );
            }*/
            return t.options[index].v;
          }

          if (tablename === "race" && isNumber(options.race)) {
            return chooseOption(options.race);
          } else if (tablename === "forcealign" && isNumber(options.alignment)) {
            return chooseOption(options.alignment);
          } else if (tablename === "hooks" && isNumber(options.plothook)) {
            return chooseOption(options.plothook);
          } else if (tablename.match(/gender$/) && isNumber(options.gender)) {
            return chooseOption(options.gender);
          }
          if (isNumber(options.subrace) &&
            (
              tablename === "raceelf" ||
              tablename === "racedwarf" ||
              tablename === "racegnome" ||
              tablename === "racehalfling" ||
              tablename === "racegenasi"
            )
          ) {
            return chooseOption(options.subrace);
          }

          if (isNumber(options.classorprof)) {
            if (tablename === "occupation") {
              return chooseOption(options.classorprof);
            } else if (
              isNumber(options.occupation1) &&
              options.classorprof === 0 &&
              tablename === "class"
            ) {
              return chooseOption(options.occupation1);
            } else if (
              isNumber(options.occupation1) &&
              options.classorprof === 1 &&
              tablename === "profession"
            ) {
              return chooseOption(options.occupation1);
            } else if (
              isNumber(options.occupation1) &&
              isNumber(options.occupation2) &&
              options.classorprof === 1 &&
              (
                tablename === "learned" ||
                tablename === "lesserNobility" ||
                tablename === "professional" ||
                tablename === "workClass" ||
                tablename === "martial" ||
                tablename === "underclass" ||
                tablename === "entertainer"
              )
            ) {
              return chooseOption(options.occupation2);
            }
          }
          return chooseRandomWithWeight(t.options, t.w);
        };
      },
      analysis: m => ({
        table: m[1]
      })
    }
  ];
