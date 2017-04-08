import React from 'react';
import { Link } from 'react-router';
import { PageHeader, Grid, Row, Col, Breadcrumb } from 'react-bootstrap';
import SongNavigation from './SongNavigation';
import { LinkContainer } from 'react-router-bootstrap';

const SongView = ({ songs, params }) => {
    const song = songs.filter(song => song._id == params.songId)[0];
    return  (      
        <Grid fluid={true} className="song-view">
            <Row>
                <Col lg={2} md={3}>
                    <SongNavigation songs={songs} />
                </Col>
                <Col lg={10} md={9}>
                    <div>
                        <input className="form-control input-lg" value={song ? song.name : ''} />                
                    </div>
                    <br />
                    <textarea value={ song ? song.tab : ''} readOnly />
                </Col>
            </Row>
            <Breadcrumb>
                <li><Link to="/a/">Home</Link></li>
                <li><Link to="/a/songs/">Songs</Link></li>
                <Breadcrumb.Item>{song ? song.name : ''}</Breadcrumb.Item>
            </Breadcrumb>   
        </Grid>
    );
}
export default SongView;