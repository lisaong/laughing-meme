const express = require('express')
const tscFinder = require('./tscs');

const app = express()

app.get('/', (req, res) => {
    let input = "Hello world";
    tscFinder.getTopN(input, 5).then(function (result, err) {
        if (err) {
            res.send(err);
        } else {
            res.send(result);
        }
    });
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
