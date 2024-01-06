import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

function SingleTodo(){
    return (
        <div>
            <TextField id="outlined-basic" label="Outlined" variant="outlined" />
            <Button variant="text">ADD</Button>
        </div>
    )
}

export default SingleTodo;