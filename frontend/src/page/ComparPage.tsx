/**Page 1: Comparison Page
 Display Review A and Review B side-by-side
 Buttons:
 A is better
 Tie
 B is better
 After voting:
 Disable vote buttons
 Display the model name

 *
 * **/
import React, { useState } from "react";
import {useNavigate} from "react-router-dom";

const ComparPage=()=>{
    const [isVote,SetIsVote]=useState(false);
    const [model,SetModel]=useState("");
    const navigat=useNavigate();
    const handleVote=(Option: "A" | "B" | "Tie" )=>{
        /** ... **/
        SetIsVote(true);

    }
    return (
        <div  style={{gap: 16}}>
            <h2>Comparison</h2>
            {/*Reviews*/}
            <div style={{display:"flex",gap: 16,margin:24,justifyContent:"center"}}>
            <div  style={boxStyle}>
                <h4>Review A</h4>
                <div style={textBox}>
                <p>Review A content</p>
                </div>
            </div>
            <div  style={boxStyle}>
                <h4>Review B</h4>
                <div style={textBox}>
                    <p>Review B content</p>
                </div>

            </div>
            </div>

            {/*Vote Button Area*/}
            <div style={{display:"flex", textAlign: "center",gap: 16,margin:24,justifyContent:"center"}}>
                <button
                    style={{minHeight:50,minWidth:50}}
                    disabled={isVote}
                    onClick={()=>{handleVote("A")}} >  A is better </button>
                <button
                    disabled={isVote}
                    onClick={()=>{handleVote("Tie")}} >Tie</button>
                <button
                    disabled={isVote}
                    onClick={()=>{handleVote("B")}} >B is better</button>
            </div>

            {/*Model Name*/}
            {isVote && <div > Model A Name:modelAName | Model B Name:modelBName</div>}
            <button style={{margin:20,minWidth:30,minHeight:30}} onClick={()=>navigat("/")}> back to Leaderboard </button>
        </div>
    )
};
const boxStyle={
    flex:1,
    border:"2px solid black",
    padding:"10px",
    minHeight:200,
}
const textBox={
    border:"2px solid black",
    padding:"10px",
    minHeight:200,
}

export default ComparPage;