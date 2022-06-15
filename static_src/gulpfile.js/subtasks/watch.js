const gulp = require('gulp');

gulp.task('watch', function() {
    gulp.watch('../static_src/oscar-refresh/scss/**/*.scss', gulp.parallel('scss'));
});
