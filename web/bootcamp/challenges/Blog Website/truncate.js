exports.summary = function (str, limit=100) {
    if (str.length > limit) {
        return str.substring(0, limit) + '...';
    } else {
        return str;
    }
}
