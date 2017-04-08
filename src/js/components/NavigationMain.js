import React from 'react';
import { Navbar, Nav, NavItem, MenuItem, NavDropdown } from 'react-bootstrap';
import { Link } from 'react-router';
import { LinkContainer } from 'react-router-bootstrap';

const NavigationMain = ({ user, auth }) => (
<Navbar inverse={true} fluid={true} fixedTop={true}>
  <Navbar.Header>
    <Navbar.Brand>
      <Link to="/a/">Tabster</Link>
    </Navbar.Brand>
  </Navbar.Header>
  <Nav>
    <LinkContainer to="/a/home">
      <NavItem>Home</NavItem>
    </LinkContainer>
    <LinkContainer to="/a/songs/">
      <NavItem>Songs</NavItem>
    </LinkContainer>
  </Nav>
  <Nav pullRight>
    <NavDropdown eventKey={3} title={user ? user.name : '...'} id="basic-nav-dropdown">
      <LinkContainer to="/a/profile">
        <MenuItem>Manage Profile</MenuItem>
      </LinkContainer>
      <MenuItem divider />      
      <MenuItem href={auth ? auth.logoutUrl : '/'}>Logout</MenuItem>      
    </NavDropdown>
  </Nav>
</Navbar>
);
export default NavigationMain;