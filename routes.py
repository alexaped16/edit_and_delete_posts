@blog.route('/edit-posts/<post_id>', methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You do not have edit access to this post.', 'danger')
        return redirect(url_for('blog.my_posts'))
    title = f"Edit {post.title}"
    form = PostForm()
    if form.validate_on_submit():
        post.update(**form.data)
        flash(f'{post.title} has been updated', 'warning')
        return redirect(url_for('blog.my_posts'))

    return render_template('post_edit.html', title=title, post=post, form=form)


@blog.route('/delete-posts/<post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You do not have delete access to this post', 'danger')
    else:
        post.delete()
        flash(f'{post.title} has been deleted.', 'secondary')
    return redirect(url_for('blog.my_posts'))