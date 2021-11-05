import React from 'react';
import { Navbar, Nav, Container, NavDropdown } from 'react-bootstrap';
import '../../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../../index.css';

class TopNavbar extends React.Component{
    render(){
        return(
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
                <Container>
                <Navbar.Brand href="#" style={{fontFamily:'Sansation-Bold', fontSize:'30px'}}>ESCAL</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="ms-auto" style={{marginRight:"20px",  marginLeft:'20px', fontFamily:'Poppins'}}>
                    <Nav.Link href="#">Home</Nav.Link>
                    <NavDropdown title="Research" id="collasible-nav-dropdown">
                        <NavDropdown.Item href="#">ESCAL Bio-Medical</NavDropdown.Item>
                        <NavDropdown.Item href="#">ESCAL Robotics</NavDropdown.Item>
                        <NavDropdown.Item href="#">ESCAL GPU</NavDropdown.Item>
                        {/* <NavDropdown.Divider />
                        <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item> */}
                    </NavDropdown>
                    <Nav.Link href="#">Event</Nav.Link>
                    <Nav.Link href="#">People</Nav.Link>
                    <Nav.Link href="#">Aboute Us</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
                
                </Container>
        </Navbar>
        );
    }
}

export default TopNavbar;