How to update blog:
-------------------

Be on the pelican-source branch 
> git checkout pelican-source

Add to content folder as needed

When finished, move to the dcc023.github.io folder and run pelican content
> pelican content

To preview, cd to the output folder, run the python -m http.server
> cd ./output
> python -m http.server

To finialize project(from the project folder)
> git push origin pelican-source
> ghp-import output
> git push https://github.com/dcc023/dcc023.github.io.git gh-pages:master

