var ss = require("sentence-similarity")
let similarity = ss.sentenceSimilarity;
let similarityScore = ss.similarityScore;
 
let s1 = "Process my data".split(" ")
let s2 = "Data design principles and strategies\nDatabase modelling techniques\nFunctions and implications of data parameters and fields\nProcesses for development of database schemas\nData warehousing concepts and methodologies".split(" ")
 
let winkOpts = { f: similarityScore.winklerMetaphone, options : {threshold: 0} }
 
console.log(similarity(s1,s2,winkOpts))