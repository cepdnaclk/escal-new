import React from 'react';
import { Carousel} from 'react-bootstrap';

import '../../index.css';
import TopNavbar from '../Navbar/Navbar';

import tempImage from '../../images/Temp.jpg';

const bodyStyle = {
    height: '100%',
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '1.5rem',
    overflow: 'hidden',
    position: 'absoulte',
}
const carouselStyle = {
    height: '80%',
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: '50px',
    position: 'relative',
}
const imgStyle = {
    height: '80vh',
    width: '100%',
    objectFit: 'cover',
}

class HomePage extends React.Component{
    render(){
        return(
            <div className={bodyStyle}>
            <TopNavbar/>
            <div className={carouselStyle}>
                <Carousel fade>
                    <Carousel.Item>
                        <img className={imgStyle}
                        src={tempImage}
                        alt="First slide"
                        />
                        <Carousel.Caption>
                        <h3>First slide</h3>
                        <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img className={imgStyle}

                        src={tempImage}
                        alt="Second slide"
                        />

                        <Carousel.Caption>
                        <h3>Second slide label</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img className={imgStyle}
                        src={tempImage}
                        alt="Third slide"
                        />

                        <Carousel.Caption>
                        <h3>Third slide label</h3>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    </Carousel>
            </div>
            </div>
        );
    }
}

export default HomePage;