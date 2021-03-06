# MarvelUS 

Canvas Group 15

---

### Introductions

- Tesia Wu
- Hannah Anees
- Helen Salgi
- Sunaina Krishnamoorthy
- Andrew Martin
- Bhavish Yalamanchi


---

### Demonstration

[Marvelus](http://marvelus.me)


---

## Self Critique

---

### What did we do well?

+++
- Intuitive design that fits our topic
  - It is instantly apparent to the user
  - Good balance: semi-minimalistic yet detailed
+++
- Easy to navigate
  - Navigation bar seen on all pages
  - Recognizable links on every page
+++
- Fun to see how everything connects
  - Easy to learn about and explore the Marvel universe  
  
---

### What did we learn?

+++
### Technical Skills
+++

- Scraping data from RESTful APIs
  - Using the Python requests library
  - Using HTTP methods like GETs and POSTs
  - Connecting our 2 different data sources through characters
  
+++
- Working with a database
  - Using MySQL and learning SQL commands
  - The flasksqlalchemy library
  - Implementing search using flask whooshalchemy
  
+++
- Creating a REST API
  - Using the flask restless library
  - Documenting an API

+++
- Using various new tools, libraries and software
  - React-Bootstrap
  - Postman
  - SQLAlchemy
  - GCP
  - and more
+++

- Hosting/managing the website
  - We learnt how to reduce costs of hosting
  - Using different production and development versions of the website

+++

- Integrating JavaScript and CSS
  - Learning how to use React
  - Using React-Bootstrap and React-Router

+++
### Other things we learnt

+++
- Working in a large team
  - Planning schedules
  - Dividing the work
+++
- Working simultaneously
  - GitHub!
  - Also dealing with git conflicts
+++
- Seeing how things connect in Marvel
  - Similarities between comic characters and movie characters
  - Watching Thor: Ragnarok!

---

### What can we do better?
+++
- Filtering
  - Could be handling multiple requests inefficiently
  - Could also not be handling requests at all after a certain amount
+++
- Design
  - Make the functionality more like the official website
  - Add movie trailers and Twitter feeds wherever possible
+++
- Nav Bar
  - When the screen size is neither large or small, the navbar extends to two lines
  - The search bar goes to the second line
  
+++
- Adding functionality
  - Trailers to the Movie and TV Show instance pages
  - Twitter feeds for Actors
  - Refactoring the website to work on mobile devices

---

### What puzzles us?
+++
- Caching
  - Browsers would cache old versions of our frontend code after deploying
+++
- Specifically searching
  - Does what it needs to do
  - But sometimes takes a long time

---

## Other Critique

Canvas Group 17 - Board Game DB

---

### What did they do well?

+++
- Pleasing design
  - Minimalistic and simple
  - Neat and well-organized
+++
- [Global search & drop-down menu](http://boardgamedb.me/)
  - Looks very professional
  - Very nice to use
+++
- Navigation
  - Smooth transitions
  - Some links connect to other sites

---

### What did we learn from their website?
+++
- More to board games than we previously thought
  - [Massive events](http://boardgamedb.me/events?per_page=18&sort=name&page=1) are held
  - Different kinds of board games are created

+++
- Filtering drop-down
  - Options are displayed in a drop-down menu
  - Also allows you to search for those selected options

---

### What can they do better?
+++
- Instance pages
  - Some pages we had to [scroll a lot](http://boardgamedb.me/genre/1002)
  - Hard to go through

+++
- Navigation
  - Some links were broken
  
+++
- Code
  - The API responses include how many pages, but not how many results 
  - When displaying related models, they were represented as lists of (id, name), instead of objects with keys and values

---

### What puzzles us about their website?
+++
- Design
  - It is a bit plain for a board game site
+++
- Pagination
  - Have to scroll quite a bit to reach the pagination bar
  - Would have been nice to either have the pagination bar at the top, or have fewer results per page
+++
- Error Handling
  - Clean up data before displaying
---


## Visualization
+++
- We created a visualization of Board Game DB's website
  - We created a stacked area chart using NVD3
  - The number of board games that were created each year are plotted against time

+++
- The visualisation shows how the genres of board games have changed over time

+++
[Visualization](http://marvelus.me/vis)
