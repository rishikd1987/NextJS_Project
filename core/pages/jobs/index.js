import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function Home({ jobs }) {
    return (
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Job Id</TableCell>
                <TableCell align="right">Summary</TableCell>
                <TableCell align="right">Job Description</TableCell>
                <TableCell align="right">Active</TableCell>
                
              </TableRow>
            </TableHead>
            <TableBody>
              {jobs.map((row) => (
                <TableRow
                  key={row.jobid}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {row.jobid}
                  </TableCell>
                  <TableCell align="right">{row.shortdescription}</TableCell>
                  <TableCell align="right">{row.detaileddescription}</TableCell>
                  <TableCell align="right">{row.is_active}</TableCell>
                  
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      );
  }

export async function getStaticProps() {
const res = await fetch("http://127.0.0.1:8000/jobs/");
const jobs = await res.json();

// const ress = await fetch("http://127.0.0.1:8000/api/category/");
// const categories = await ress.json();

return {
    props: {
    jobs,
    },
};
}

export default Home;