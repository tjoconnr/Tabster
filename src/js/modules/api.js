const APIKEY = 'ahFkZXZ-b21lZ2EtdGFic3RlcnIRCxIEVXNlchiAgICAgODXCAw';
const API = {
    doFetch(url){
        const fetchSettings = {
            method: 'GET',
            headers: new Headers({
                'Authorization': APIKEY
            }),
            mode: 'cors',
            cache: 'default' 
        };
        return fetch(url, fetchSettings).then(resp => {
            if (resp.ok) {
                return resp.json();
            }
        }).then(obj => {
            console.log(obj);
            return obj;
        });
    },
    fetchUser(){
        return this.doFetch('/api/v1/user');
    },
    fetchAuth(){
        return this.doFetch('/api/v1/authorize');
    },
    fetchSongs(){
        return this.doFetch('/api/v1/song');
    },
    fetchSong(songId){
        return this.doFetch('/api/v1/song/'+songId);
    },
};
export default API;