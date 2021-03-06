import React from 'react'
import {Carousel, Container, Slide} from 'react-bootstrap'

var imageStyles = {
    height: "850px",
    width: "1700px"
}

var headerStyle={
    fontSize: '300px',
    color: 'black',
    textDecoration: 'bold',
    textShadow: '2px 1px gray',
    textAlign: 'center',
    opacity: '0.0',
}


class Home extends React.Component {
    render() {
        return (
            <div>
            
                <Carousel controls={false}>
                    <Carousel.Item>
                        <img className="center-block" alt="900x500"
                             src="http://cdn2us.denofgeek.com/sites/denofgeekus/files/2017/06/spider-man_homecoming_reboot_box_office.jpg"
                             style={imageStyles}/>
                    </Carousel.Item>
                    <Carousel.Item animateIn>
                        <img className="center-block" alt="900x500"
                             src="http://static.comicvine.com/uploads/original/9/99801/2244678-23308595.png"
                             style={imageStyles}/>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img className="center-block" alt="900x500"
                             src="https://s3.amazonaws.com/libapps/accounts/36130/images/marvel.jpeg"
                             style={imageStyles}/>
                    </Carousel.Item>
                </Carousel>

                <div>
            <h1 style={headerStyle}><b>MARVELUS</b></h1>
                    
                </div>
            </div>
        )
    }
}

export default Home
