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
exports.getTopN = async function(input, count) {
    try {
        const url = "https://raw.githubusercontent.com/lisaong/data/master/tscs/skillsmap_table.json";
        const response = await fetch(url);
        const json = await response.json();

        return getTopMatches(json, input, count);

    } catch (error) {
        console.log(error);
    }
}

function getTopMatches(data, input, n) {
    const similarity = ss.sentenceSimilarity;
    const similarityScore = ss.similarityScore;

    const winkOpts = { f: similarityScore.winklerMetaphone, options : {threshold: 0} };

    let tscs = [];
    data.forEach(element => {
        let knowledge = element.Knowledge.split(" ")
        let abilities = element.Abilities.split(" ")
        let splitInput = input.split(" ");

        let score = similarity(splitInput, knowledge, winkOpts).score;
        tsc = JSON.stringify(element)
        tscs.push({"score": score, "tsc" : tsc });
        score = similarity(splitInput, abilities, winkOpts).score;
        tscs.push({"score": score, "tsc" : tsc });
    });

    // sort by highest scores
    return _.sortBy(tscs, 'score').reverse().slice(0, n);
}
