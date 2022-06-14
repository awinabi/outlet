const gulp = require("gulp");

module.exports = function(done) {
    // Copy all tracked static files into the build directory
    gulp.src("oscar-refresh/**/*")
        .pipe(gulp.dest("../static/oscar-refresh/"));

    // Copy all third party assets in to the build directory
    gulp.src("node_modules/jquery/dist/jquery.min.js")
        .pipe(gulp.dest("../static/oscar-refresh/js/jquery"));

    gulp.src([
        "node_modules/bootstrap/dist/js/bootstrap.bundle.js",
        "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js"
    ]).pipe(gulp.dest("../static/oscar-refresh/js/bootstrap"));

    gulp.src("node_modules/bootstrap/fonts/*")
        .pipe(gulp.dest("../static/oscar-refresh/fonts/"));

    gulp.src("node_modules/inputmask/dist/jquery.inputmask.min.js")
        .pipe(gulp.dest("../static/oscar-refresh/js/inputmask"));

    gulp.src("node_modules/jquery-mousewheel/jquery.mousewheel.js")
        .pipe(gulp.dest("../static/oscar-refresh/js/mousewheel"));

    gulp.src("node_modules/jquery-sortable/source/js/jquery-sortable-min.js")
        .pipe(gulp.dest("../static/oscar-refresh/js/jquery-sortable"));

    gulp.src("node_modules/@fortawesome/fontawesome-free/webfonts/*")
        .pipe(gulp.dest("../static/oscar-refresh/webfonts"));

    done();
};
