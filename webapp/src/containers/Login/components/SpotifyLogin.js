import React, { Component } from 'react';
import { clientId, redirectUri } from '../../../utils/config';
import logo from '../../../assets/imgs/spotify_logo.png';
import './index.css'

export class SpotifyLogin extends Component {

    scopes = [
        'playlist-modify-public',
        'user-read-private',
        'user-read-email'
    ]

    render () {
        const response_type = 'code';
        const scope = this.scopes.join(' ');

        const host = 'accounts.spotify.com';
        let path = 'authorize/?';
        path += `client_id=${clientId}&`;
        path += `response_type=${response_type}&`;
        path += `redirect_uri=${redirectUri}&`;
        path += `scope=${scope}&`;
        path += `show_dialog=${true}`;

        const uri = `https://${host}/${path}`;

        return(
            <a href={uri} className="SpotifyLogin">
                <div className="SpotifyLogo">
                    <img src={logo} alt="weltfy" />
                </div>
                <div className="SpotifyLink">
                    {`login here`}
                </div>
            </a>
        );
    }
}

export default SpotifyLogin;