const express = require('express')
const tscFinder = require('./tscs');

const app = express()

app.get('/', (req, res) => {

    let input = "Hello world";
    let result = await tscFinder.getTopTscMatches(input);
    res.send();
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
