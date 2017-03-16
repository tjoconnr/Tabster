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
		<Link to="/a/songs/">Songs</Link>
	</Grid>
);
export default Home;

