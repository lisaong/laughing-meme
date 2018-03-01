const assert = require('assert');
const tscFinder = require('../tscs');

describe('tscFinder', function() {
  describe('#getTopN()', function() {
    it('should find at least 1 score', function(done) {
        // query can be slow
        this.timeout(20000); // msec

        tscFinder.getTopN("Hello world", 5).then(function (result, err) {
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