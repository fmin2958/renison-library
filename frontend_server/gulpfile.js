// Include Gulp
var gulp = require('gulp');

// Include plugins
var concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    minifyCss = require('gulp-minify-css');

var dest = 'public';

// Concatenate & Minify JS
gulp.task('minify-js', function() {
    return gulp.src('js/**')
        .pipe(concat('main.js'))
        .pipe(uglify())
        .pipe(gulp.dest(dest));
});

gulp.task('minify-css', function() {
    return gulp.src('styles/*.css')
        .pipe(minifyCss())
        .pipe(gulp.dest(dest));
});

gulp.task('minify', ['minify-js', 'minify-css']);
