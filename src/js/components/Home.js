import React from 'react';
import { PageHeader, Grid, Breadcrumb, Row, Col, Jumbotron } from 'react-bootstrap';
import { Link } from 'react-router';

import SongNavigation from './SongNavigation';

const Home = ({ user }) => (
    <Grid>
        <br /><br />
        <br /><br />
        <br /><br />
        <Row>
            <Col lg={4} offsetLg={2}>
                <div className='animated zoomInDown text-right'>
                    <img src="/img/labtocat.png" />
                </div>
            </Col>
            <Col lg={4}>
                <div className='animated zoomInDown'>
                    <h1>Welcome to Tabster.</h1>
                    <br /><br />
                    <Link to='/a/songs/' className='btn btn-primary btn-lg'>Browse Songs</Link>
                </div>
            </Col>
        </Row>
    </Grid>
);
export default Home;

