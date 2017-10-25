import React from 'react'
import { Link } from 'react-router-dom'

export default class Characters extends React.Component {
    constructor(props) {
        super(props);
        this.state = {characters: []}
    }

    componentDidMount() {
        $.getJSON(document.location.origin + '/api/character')
            .then((data) => {
                this.setState({characters: data});
            });
    }

    render() {
        const characters = this.state.characters.map((item, i) => {
            return(
                <div key = {item.id} className="item col-xs-6 col-lg-4">
                    <div className="card thumbnail">
                        <div className="card-img center-cropped"
                            style={{backgroundImage: 'url(' + item.image_url + ')'}}/>
                        <div className = "caption">
                            <h4 className="group inner list-group-item-heading">{item.name}</h4>
                        </div>
                    </div>
                </div>

                );
        });
        return (
            <div>
                <div className="container">
                    <div id="tvshow" className="row list-group">
                        { brands }
                    </div>
                </div>
            </div>

        );
    }
}