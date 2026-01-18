import React, { useEffect, useState } from 'react';

const Activities = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : '/api/activities/';
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
        console.log('Endpoint used:', endpoint);
      });
  }, [endpoint]);

  return (
    <div className="row justify-content-center">
      <div className="col-md-10">
        <div className="card shadow-sm mb-4">
          <div className="card-body">
            <h2 className="card-title mb-4">Activities</h2>
            <div className="table-responsive">
              <table className="table table-striped table-hover align-middle">
                <thead className="table-primary">
                  <tr>
                    <th>#</th>
                    <th>User</th>
                    <th>Workout</th>
                    <th>Duration (min)</th>
                  </tr>
                </thead>
                <tbody>
                  {activities.map((a, i) => (
                    <tr key={a.id || i}>
                      <td>{i + 1}</td>
                      <td>{a.user?.name || a.user}</td>
                      <td>{a.workout?.name || a.workout}</td>
                      <td>{a.duration}</td>
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

export default Activities;
