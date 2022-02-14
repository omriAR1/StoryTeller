import React, { Component } from 'react';

class SearchBox extends Component {
    constructor(props) {
        super(props);
        this.state = {value: this.props.searchField};
    
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        this.setState({value: event.target.value});
        this.props.searchField = this.state.value;
    }
        
    render() {
        return (
            <div>
                <input type="text"
                       value={this.state.value}
                       name="search-input" 
                       id="serach-text" 
                       className="input border border-gray-400 appearance-none rounded px-3 py-3 pt-3 pb-3 focus focus:border-indigo-600 focus:outline-none active:outline-none active:border-indigo-600" 
                       placeholder="book name"
                       onChange={this.props.change}>
                </input>
                <p>{this.state.value}</p>
            </div>
        );
    }
}

export default SearchBox;
