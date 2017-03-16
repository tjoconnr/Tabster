import React from 'react';
import { PageHeader, Grid, Breadcrumb } from 'react-bootstrap';
import { Link } from 'react-router';

import SongNavigation from './SongNavigation';

const Home = ({ user }) => (
	<Grid fluid={true}>
		<Breadcrumb>
            <Breadcrumb.Item>
                Home
            </Breadcrumb.Item>
        </Breadcrumb>
		<PageHeader>Welcome { user ? user.name : ''}</PageHeader>        
        <img src={user ? user.avatar : null } className="img-circle" />
		<Link to="/a/songs/" className="btn btn-default btn-lg">Browse Songs</Link>
	</Grid>
);
export default Home;

