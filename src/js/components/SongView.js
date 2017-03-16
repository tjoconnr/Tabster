import React from 'react';
import { Link } from 'react-router';
import { PageHeader } from 'react-bootstrap';


const SongView = ({ songs, params }) => {
	const song = songs.filter(song => song._id == params.songId)[0];
	return  (
	  <div>      
	    <Link to='/a/'>Back to songs</Link>
	    <PageHeader>{song ? song.name : '...'}</PageHeader>
	    <pre>
	    	{ song ? song.tab : ''}
	    </pre>
	  </div>   
	);
}
export default SongView;