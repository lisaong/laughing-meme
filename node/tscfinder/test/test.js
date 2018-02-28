const assert = require('assert');
const tscFinder = require('../tscs');

describe('tscFinder', function() {
  describe('#getTopN()', function() {
    it('should find at least 1 score', function(done) {
        const input = "Hello world";
        tscFinder.getTopN(input, 5).then(function (result, err) {
            if (err) {
                done(err);
            } else {
                assert.equal(result.length, 5);
                assert.equal(result[0].score > 0, true);
                done();
            }
        });
    });
  });
})