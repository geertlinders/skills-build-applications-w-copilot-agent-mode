import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
    : '/api/leaderboard/';
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Fetched leaderboard:', results);
        console.log('Endpoint used:', endpoint);
      });
  }, [endpoint]);

  return (
    <div className="row justify-content-center">
      <div className="col-md-8">
        <div className="card shadow-sm mb-4">
          <div className="card-body">
            <h2 className="card-title mb-4">Leaderboard</h2>
            <div className="table-responsive">
              <table className="table table-striped table-hover align-middle">
                <thead className="table-primary">
                  <tr>
                    <th>#</th>
                    <th>User</th>
                    <th>Score</th>
                  </tr>
                </thead>
                <tbody>
                  {leaderboard.map((l, i) => (
                    <tr key={l.id || i}>
                      <td>{i + 1}</td>
                      <td>{l.user?.name || l.user}</td>
                      <td>{l.score}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
