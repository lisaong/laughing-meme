const fetch = require("node-fetch");
const ss = require("sentence-similarity");
const _ = require('underscore-node');

// TODO:
// input sentence as post request
// componentize
// Mocha test
// CI/CD
// try natural

// Load json entries
exports.getTopTscMatches = async function(input) {
    try {
        const url = "https://raw.githubusercontent.com/lisaong/data/master/tscs/skillsmap_table.json";
        const response = await fetch(url);
        const json = await response.json();

        return getTopMatches(json, input);

    } catch (error) {
        console.log(error);
    }
}

function getTopMatches(data, input) {
    const similarity = ss.sentenceSimilarity;
    const similarityScore = ss.similarityScore;
    
    const winkOpts = { f: similarityScore.winklerMetaphone, options : {threshold: 0} };

    let tscs = [];
    data.forEach(element => {
        let knowledge = element.Knowledge.split(" ")
        let abilities = element.Abilities.split(" ")
        let splitInput = input.split(" ");

        let score = similarity(splitInput, knowledge, winkOpts).score;
        tscs.push({"score": score, "tsc" : element });
        score = similarity(splitInput, abilities, winkOpts).score;
        tscs.push({"score": score, "tsc" : element });
    });

    // sort by highest scores
    console.log(_.sortBy(tscs, 'score').reverse().slice(0, 10));
}