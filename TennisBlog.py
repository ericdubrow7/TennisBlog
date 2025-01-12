from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts
posts = [
    {
        'title': 'US Open 2024: Exciting Quarterfinal Matches',
        'author': 'John Doe',
        'date': 'September 15, 2024',
        'content': 'The US Open quarterfinals are packed with thrilling matches...'
    },
    {
        'title': 'Wimbledon 2024: Djokovic Eyes Another Title',
        'author': 'Jane Smith',
        'date': 'July 10, 2024',
        'content': 'Novak Djokovic is ready to defend his Wimbledon crown...'
    },
    {
        'title': 'US Open 2023: Carlos Alcaraz Defends His Title in Thrilling Five-Set Final',
        'author': 'Eric Dubrow',
        'date': 'September 15, 2024',
        'content': "The 2024 US Open concluded with an exhilarating final as Spain’s Carlos Alcaraz successfully defended his title in an epic five-set match against Norway’s Casper Ruud. Alcaraz, who has been a rising star in tennis over the last few years, showcased his resilience and fighting spirit to secure his second consecutive US Open trophy. In front of a packed Arthur Ashe Stadium, Alcaraz triumphed 6-4, 3-6, 7-6 (7-5), 2-6, 6-3, solidifying his position as one of the top contenders in the sport. This victory brings his Grand Slam tally to three, further solidifying his status as a future legend in men’s tennis."   
    },
    {
        'title': 'US Open 2023: Carlos Alcaraz Defends His Title in Thrilling Five-Set Final',
        'author': 'Eric Dubrow',
        'date': 'September 15, 2024',
        'content': "The 2024 US Open concluded with an exhilarating final as Spain’s Carlos Alcaraz successfully defended his title in an epic five-set match against Norway’s Casper Ruud. Alcaraz, who has been a rising star in tennis over the last few years, showcased his resilience and fighting spirit to secure his second consecutive US Open trophy. In front of a packed Arthur Ashe Stadium, Alcaraz triumphed 6-4, 3-6, 7-6 (7-5), 2-6, 6-3, solidifying his position as one of the top contenders in the sport. This victory brings his Grand Slam tally to three, further solidifying his status as a future legend in men’s tennis."   
    },
    {
        'title': 'US Open 2023: Carlos Alcaraz Defends His Title in Thrilling Five-Set Final',
        'author': 'Eric Dubrow',
        'date': 'September 15, 2024',
        'content': "The 2024 US Open concluded with an exhilarating final as Spain’s Carlos Alcaraz successfully defended his title in an epic five-set match against Norway’s Casper Ruud. Alcaraz, who has been a rising star in tennis over the last few years, showcased his resilience and fighting spirit to secure his second consecutive US Open trophy. In front of a packed Arthur Ashe Stadium, Alcaraz triumphed 6-4, 3-6, 7-6 (7-5), 2-6, 6-3, solidifying his position as one of the top contenders in the sport. This victory brings his Grand Slam tally to three, further solidifying his status as a future legend in men’s tennis."   
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id]
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
