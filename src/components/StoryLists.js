import React, { Component } from 'react';
import StoryCard from './StoryCard';
import SearchBox from './SearchBox';

class StoryLists extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            items: props.items,
            itemsNum: props.items.length,
            cards_data: props.items, 
            searchField: '',
            cardsArray: '', 
        }
 
        
    }

    searchChange(event) {
        this.setState({searchField: event.target.value})
    }

    render() {
        
        const filtered_results = this.state.items.filter( book => {
                return book.name.toLowerCase().includes(this.state.searchField.toLowerCase())
        });

        const cards_blocks = filtered_results.map(it => {
            return (
            <StoryCard id={it.id}
             key={it.id}
             name={it.name} 
             ganere={it.ganere} 
             correlation={it.percentage}
            />
            )
        })

        return (
            <div>
                <p>search a book by name: <SearchBox 
                        search={this.state.searchField} change={this.searchChange.bind(this)}/></p>
                <p>{this.state.searchField}</p>
                <h3> Items: {this.state.itemsNum}</h3>
                <div className="display-cards">
                    <table className="table-auto">
                        <thead>
                            <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Author</th>
                            <th>Year</th>
                            <th>Ganere</th>
                            <th>Correaltion</th>
                            </tr>
                        </thead>
                        <tbody>
                            {cards_blocks}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
}

export default StoryLists;