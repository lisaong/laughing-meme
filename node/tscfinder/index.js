const express = require('express')
const bodyParser = require('body-parser');
const tscFinder = require('./tscs');

const app = express()
app.set('view engine', 'pug')
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/assets', express.static('assets'))
app.use('/images', express.static('images'))

app.get('/', (req, res) => {
    res.render('index', {
        title: 'TSC Finder',
        message: 'Enter your description to find TSCs using semantic analysis.'
    })
});

app.post('/', (req, res) => {
    let input = req.body.text;
    const n = 5;
    tscFinder.getTopN(input, n).then(function (results, err) {
        if (err) {
            res.send(err);
        } else {
            res.render('results', {
                title: 'TSC Finder Results',
                message: 'Top ' + n + ' results',
                input: 'Query: ' + input,
                results: results })
        }
    });
});

app.listen(3000, () => console.log('Example app listening on port 3000!'))
