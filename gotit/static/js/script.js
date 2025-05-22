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