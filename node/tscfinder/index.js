const fetch = require("node-fetch");
const ss = require("sentence-similarity")

// TODO:
// Mocha test
// CI/CD
// input sentence
// try natural

// Load json entries
const url = "https://raw.githubusercontent.com/lisaong/data/master/tscs/skillsmap_table.json";

const getLocation = async url => {
    try {
        const response = await fetch(url)
        const json = await response.json()

        let input = "".split(" ")
        getTopMatches(json, input)

    } catch (error) {
        console.log(error)
    }
}

function getTopMatches(data, input) {
    const similarity = ss.sentenceSimilarity;
    const similarityScore = ss.similarityScore;
    
    let winkOpts = { f: similarityScore.winklerMetaphone, options : {threshold: 0} }

    let scores = {}
    data.forEach(element => {
        
    });

    console.log(similarity(s1,s2,winkOpts))

}

getLocation(url)
