import React, { useState } from 'react';
import queryString from 'query-string';
import countries from '../../assets/jsons/spotify_countries.json'

function Selection(props) {
    
    const [country, setCountry] = useState('')
    const token = queryString.parse(props.location.search).code
    
    function handleSubmit(event) {
        event.preventDefault()

        fetch('/playlist', {
            method:'POST',
            cache:'no-cache',
            headers:{
                'content_type': 'application/json',
            },
            body:{
                'country':country,
                'token': token,
            }
        }).then(response => {
            console.log(response.json())
        }).then(data => {
            console.log(data.url)
        })
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Select the country:
                    <select value={country} onChange={event => setCountry(event.target.value)}>
                        {countries['countries'].map((country, index) => {
                            return <option key={country.toString()} value={country}>{country}</option>
                        })}
                    </select>
                </label>
                <input type="submit" value="Go!" />
            </form>
        </div>
    );
}

export default Selection;
