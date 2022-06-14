const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps');
const pump = require('pump');

module.exports = function(cb) {
    pump(
        [
            gulp.src('oscar-refresh/scss/dashboard.scss'),
            sourcemaps.init(),
            sass({
                includePaths: [
                    'oscar/scss/',
                ],
                outputStyle: null,
            }),
            sourcemaps.write('/'),
            gulp.dest('../static/oscar-refresh/css/')
        ],
        cb
    );
};
