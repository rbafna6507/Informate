import './App.css';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger'
import Popover from 'react-bootstrap/Popover'
import Navbar from 'react-bootstrap/Navbar'

class NewStory extends React.Component {
  render() {
      return (
        <OverlayTrigger
          trigger = {['hover', 'focus']}
          placement = 'right'
          overlay = {(
            <Popover>
              <Popover.Header as='h3'>{this.props.source}</Popover.Header>
              <Popover.Body>{this.props.content}</Popover.Body>
            </Popover>
          )}
        >
          <li>
            <a href = {this.props.link}>{this.props.headline}</a>
          </li>
        </OverlayTrigger>
      );
  }
}

// originally thought code would be more organized and would require
// another React Component for each source (best solution for flexible + dynamic coding)
// but easiest solution for this project is to hard code in it's locations because
// of time + lack of further development.

// class NewSource extends React.Component {

//   render() {
//       return (
//           // some kind of four loop that creates a new Story for each article in this.state.articles
//           <ul>
//             <NewStory />
//           </ul>
//       );
//   }
// }



class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      data : [],
      numChildren : 0,
    }
  }

// using .then to go deeper into the api response.
// then using the callback function for this.setState in order to print this.state.data once state is updated
  componentDidMount() {
    fetch('https://newsaggregator-api.herokuapp.com/')
      .then(resp => resp.json())
      .then((story) => {
        this.setState({
          data: story
          })
      })
  }
  
  // run didmount
  // send to state
  // if exist:
    // display info as list ellement
  render() {
    let article_array = this.state.data
    if (this.state.data.length !== 0) {
      console.log('this.state.data has things');
      return (
        <div style = {{display: 'inline-block',
                       width: 550}}
        >
          <Navbar style = {{width:'100vw'}} bg="light" variant="light">
            <h1>Informate</h1>
          </Navbar>
          <h4 style = {{paddingLeft:20,
                        paddingTop: 20}}>New York Times</h4>
          <ul>
            {article_array.slice(0, 6).map((item, index) => {
              return (
                <NewStory key = {index} 
                          link = {item['link']}
                          content = {item['info']}
                          headline = {item['headline']}
                          source = {item['source']}/>
              );
            })}
          </ul>
          <h4 style = {{paddingLeft:20,
                        paddingTop: 20}}>Reuters</h4>
          <ul>
            {article_array.slice(6, 12).map((item, index) => {
              return (
                <NewStory key = {index} 
                          link = {item['link']}
                          content = {item['info']}
                          headline = {item['headline']}
                          source = {item['source']}/>
              );
            })}
          </ul>
          <h4 style = {{paddingLeft:20,
                        paddingTop: 20}}>Wired</h4>
          <ul>
            {article_array.slice(12, 18).map((item, index) => {
              return (
                <NewStory key = {index} 
                          link = {item['link']}
                          content = {item['info']}
                          headline = {item['headline']}
                          source = {item['source']}/>
              );
            })}
          </ul>
          <h4 style = {{paddingLeft:20,
                        paddingTop: 20}}>The Economist</h4>
          <ul>
            {article_array.slice(18, 24).map((item, index) => {
              return (
                <NewStory key = {index} 
                          link = {item['link']}
                          content = {item['info']}
                          headline = {item['headline']}
                          source = {item['source']}/>
              );
            })}
          </ul>
          <h4 style = {{paddingLeft:20,
                        paddingTop: 20}}>BBC</h4>
          <ul>
            {article_array.slice(24, 30).map((item, index) => {
              return (
                <NewStory key = {index} 
                          link = {item['link']}
                          content = {item['info']}
                          headline = {item['headline']}
                          source = {item['source']}/>
              );
            })}
          </ul>
        </div>
      );
    }
    return (
      <h1>Informate</h1>
    )
  }
}


export default App;

