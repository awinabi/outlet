const gulp = require('gulp');

gulp.task('watch', function() {
    gulp.watch('oscar-refresh/scss/**/*.scss', gulp.parallel('scss'));
});
