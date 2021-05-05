import { notDeepStrictEqual } from 'assert';
import {generate} from './generate';
import {printNPC} from './utils';
import {Npc} from './index'
const mongodb = require('mongodb');

// Initialize globals
let options = {
    race:           null,
    subrace:        null,
    classorprof:    null,
    occupation1:    null,
    occupation2:    null,
    alignment:      null,
    plothook:       null,
    gender:         null,
}


// Parse CLI args
const args = process.argv;
let schema = 'npc';
let N = 1;
if (args.length > 2) {
    schema = args[2]
}
if (args.length > 3) {
    N = Number(args[3])
}


// Generate N NPCs
let start = new Date().getTime()
let npcs = []
for (let i = 0; i < N; i++) {
    let npc = generate(schema, options)
    npcs.push(npc.npc)
}
let end = new Date().getTime()
console.log(`Generated ${npcs.length} NPCs in ${end-start} ms`)


//console.log(npcs)

// Print the NPC description
// npcs.forEach(npc => { printNPC(npc) });


// Write to DB
let MongoClient = mongodb.MongoClient;
let url = "mongodb://localhost:27017/";
let start2 = new Date().getTime()
MongoClient.connect(url, { useUnifiedTopology: true } , function(err, db) {
  if (err) throw err;

  var dbo = db.db("dnd");

  var myobj = npcs[0];
  dbo.collection("npc").insertMany(npcs, function(err, res) {
    if (err) throw err;
    let end2 = new Date().getTime()
    console.log(`Inserted ${res.insertedCount} NPCs into DB ${end2-start2} ms`)
    db.close();
    
  });
});








