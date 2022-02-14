import React, { Component } from 'react';
import StoryLists from './StoryLists';
import './StoryTeller.css';
import MySvg from './Wave';

const fake_date = [
    {
        id:0,
        name:'The Sliding Mr. Bones (Next Stop, Pottersville)',
        author:	'Malcolm Lockyer',
        year: 1961,
        ganere: 'darama',
        percentage: 100
    },
    {   
        id:1,
        name:'The Slidingop, Pottersville)',
        author:	'Malcockyer',
        ganere: 'action',
        year: 1968,
        percentage: 65
    },
]

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = 
        {   date: new Date(),
            numOfCards: 20,
            fake_date
        };
    }


    render() {
        return (
            <div className="app-main text-center"
            style={{ backgroundImage: `url(${<MySvg />})` }}>
                <h1 className="main-title text-3xl">Welcome to Story Teller!</h1>
                <p>This project aims to find correaltion in stories.</p>
                <StoryLists items={this.state.fake_date}/>
            </div>
        );
    }
}

export default Home;
