import {useNavigate} from "react-router-dom";

/**
 *
 * Page 2: Leaderboard
 * Display ranked models
 * Sorted by votes descending
 * No advanced styling required.
 * **/
type ModelScore={
    modelName:string;
    votes:number;
};

const Leaderboard=()=>{
    const navigate=useNavigate();
    const data:ModelScore[]=[
        {modelName:"GPT-4",votes:10},
        {modelName:"Gmini-3.0",votes:9},
        {modelName:"Clouder",votes:9}
    ];

    const sortData= [...data].sort((a,b)=> b.votes-a.votes);
    return(
        <div style={{ padding: 24 }}>
            <h2>Leaderboard</h2>
            <div style={{border:"2px solid #000"}}>
            <table style={{
                alignItems:'center',
                left:'auto',
                justifyContent:'space-between',
                width: "100%",
                minHeight:400,
            }}>
                <thead>
                <tr>
                    <th style={thStyle}>Rank</th>
                    <th style={thStyle}>Model</th>
                    <th style={thStyle}>Votes</th>
                </tr>
                </thead>
                <tbody>
                    {sortData.map((item,index)=>(
                        <tr style={{border:"2px solid #000",gap:10}} key={item.modelName}>
                            <th style={tdStyle}>{index+1}</th>
                            <th style={tdStyle}>{item.modelName}</th>
                            <th style={tdStyle}>{item.votes}</th>
                        </tr>
                    ))}
                </tbody>
            </table>
            </div>
            <button style={{margin:20}}
                    onClick={()=>navigate("/comparpage" )}> to Comparison </button>
        </div>
    );

};

const thStyle: React.CSSProperties = {
    border: "1px solid black",
    padding: 8,

};

const tdStyle: React.CSSProperties = {
    border: "1px solid black",
    padding: 8,
};
export default Leaderboard;