// javascript for search button in jobspage
document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById('jobSearchInput');
  const searchBtn = document.getElementById('jobSearchBtn');
  const jobItems = document.querySelectorAll('.job-list-item');

  function filterJobs() {
    const query = searchInput.value.trim().toLowerCase();
    jobItems.forEach(item => {
      // Collect all searchable fields
      const text = (
        item.dataset.company + " " +
        item.dataset.role + " " +
        item.dataset.location + " " +
        item.dataset.salary + " " +
        item.dataset.description
      );
      if (text.includes(query)) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }

  // Filter as user types
  searchInput.addEventListener('input', filterJobs);
  // Filter on button click
  searchBtn.addEventListener('click', filterJobs);
});

// javascript for applied job
document.addEventListener('DOMContentLoaded', function() {
    // Notification toggle
    const notifBtn = document.getElementById('notifBtn');
    const notifications = document.getElementById('notifications');
    notifBtn.addEventListener('click', function() {
        notifications.style.display = (notifications.style.display === 'none') ? 'block' : 'none';
    });

    // Applied Jobs toggle
    const showBtn = document.getElementById('showAppliedBtn');
    const cards = document.getElementById('appliedJobsCards');
    let shown = false;
    showBtn.addEventListener('click', function() {
        shown = !shown;
        cards.style.display = shown ? 'block' : 'none';
        showBtn.textContent = shown ? 'Hide Applied Jobs' : 'Show Applied Jobs';
    });
});
