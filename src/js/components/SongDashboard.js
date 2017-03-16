import React from 'react';
import { PageHeader, Grid, Breadcrumb } from 'react-bootstrap';
import { Link } from 'react-router';

import SongNavigation from './SongNavigation';

const SongDashboard = ({ songs }) => (
	<Grid fluid={true}>
		<Breadcrumb>
            <li><Link to="/a/home">Home</Link></li>
            <Breadcrumb.Item>
                Songs
            </Breadcrumb.Item>           
        </Breadcrumb>
		<PageHeader>Songs{ songs ? ': ' + songs.length : null } </PageHeader>
		<SongNavigation songs={songs} />
	</Grid>
);
export default SongDashboard;

