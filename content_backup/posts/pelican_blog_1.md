Title: Rise of the Pelican
Category: python
Date: 2018-08-24
Modified: 2018-08-24
Tags: framework, pelican, python, static, site, generator
Slug: rise-of-the-pelican
Authors: Dylan Campbell
Summary: Using the Pelican static site generator

# Preface
Most of you have probably heard/worked with Django, Flask, or Ruby on Rails, but I'm sure only a few have heard of Pelican. Pelican is not a full-fledged web framework. It is an extremely light weight alternative, a static site generator. It's main focus is to easily generate static websites without having to worry about maintaining a backend. So for the purposes of maintaining a personal website, it has most everything I need.

As a fresh college graduate in my first software developer job, I have decided to begin working on my professional online image. I worked on my LinkedIn account, started cleaning up my github, and have decided to fix up my personal website. I use the github.io site since it is free and simple to interface with via git commands. 

Up to this point, I have had a personal website, but it was a mess. I would experiment with various html/css/javascript tricks to see what I could accomplish. As much fun as it was, it looked like crap. When I decided to clean things up, I wanted to find a way to use python to generate the website so that I would not have to write all of the html and css by hand. 

I came across the greats of web frameworks in my searches but found them to be a little overkill. Seeing as I wanted a simple blog with an about and contact page. This is when I came across what are called static site generators. They are built to easily/efficiently handle my exact usecase (Wow, so you mean I'm not unique? /s). When searching through the list of them, I found Pelican to be the most kept up with python-based one. That is when I bit the bullet and decided to actually start working on the site.

![Pelican Image](https://www.fullstackpython.com/img/logos/pelican.png)

To start things off, I hopped right into the [Quickstart Guide](http://docs.getpelican.com/en/stable/quickstart.html) on the Pelican documentation. Got it up and running in less than 5 minutes, ez. 

Next I wanted to create a page and see what that was all about since that is what I would most always being doing. I began working through the [Full Stack Python tutorial](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html). Quickly realized that this tutorial was not created with Windows in mind. So I would have to translate on the fly, which is always risky when learning something new. Pelican initialization gives you a nice handy makefile, but I did not want to get too reliant on using a buildfile when I hardly know the commands. 

```python
# Commands that are commonly used.

pelican ./content # Generates the website using the content folder.

python -m http.server # Run from within output folder, serves website to localhost:8000
```

(After a bit, I just created a batch file that handles this.)

So far I was understanding the basics. Pelican generates the website and places all of the files into the output folder. This output folder has everything needed to display the website in a nice organized fashion. You should not be editing anything in the output folder. 

What does it generate it from, you ask? Pelican uses the *content folder* to know what content to generate. Content meaning all of the blogs and pages you will want to add to the site. If you want to create static pages such as an about page, you would create a subfolder named *pages* within the *content folder*. Within this *pages folder*, you can create a markdown file and write whatever info you want. Next time you generate, Pelican will see that file and give it its own route and (theme-dependent) add it to the toolbar on all the other webpages. How sweet of it.

For writing blog posts, it handles this very well. Create a subfolder named *posts* within the *content folder*. This is where you will place all of your blog entries (You can further diversify from there, but we will not get into that). It will organize these posts by utilizing the information placed in the header tags.

```
Title: Rise of the Pelican
Category: python
Date: 2018-08-24
Modified: 2018-08-24
Tags: framework, pelican, python, static, site, generator
Slug: rise-of-the-pelican
Authors: Dylan Campbell
Summary: Using the Pelican static site generator
```

Aside from adding content, you also will need to edit the pelicanconf.py file on occasion. Its simply formatted, so you can parse down it and figure out what you'd need to change. I learned that a blog roll is a list of links where you advertise other blogs.

At this point, I had it up and running. I made a sample blog and was geniunely impressed by Pelicans simplicity. Next on the agenda was to change the theme. I did not want to just rock the default pelican theme, which is not ugly by any means. I headed over to [Pelican Themes](http://www.pelicanthemes.com/) and decided on using the [pelican-blue](https://github.com/parbhat/pelican-blue) theme. It is simple, professional, and mobile friendly.

The way you utilize the theme is to clone the theme repo into the Pelican project folder (I created a pelican-themes folder in the project, then cloned the pelican-blue repo into it, to be more organized.) Then from within the pelicanconf.py file, place 
`THEME = 'pelican-themes/pelican-blue'` 
somewhere within it. Then generate the website and it'll be looking nice and new without having to change the file structure.

After creating the About and Contact pages, we have the website looking nice and clean. All that is left is to fill it with meaningful content. Starting with this post!


