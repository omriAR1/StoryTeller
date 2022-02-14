import React, { Component } from 'react';

class StoryCard extends Component {
    render() {
        return (   
            <tr>
                <td>{this.props.id}</td>
                <td>{this.props.name}</td>
                <td>Malcolm Lockyer</td>
                <td>1961</td>
                <td>{this.props.ganere}</td>
                <td>{this.props.correlation}</td>
            </tr>
        );
    }
}

export default StoryCard;
