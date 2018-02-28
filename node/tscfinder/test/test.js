const assert = require('assert');
const tscFinder = require('../tscs');

console.log(tscFinder);

describe('getTopMatches', function() {
  describe('#shouldFindScores()', function() {
    it('should find at least 1 score', function() {
        const input = "Hello world";
        const result = tscFinder.getTopTscMatches(input);
        assert.equal(result.length > 0, true);
    });
  });
})