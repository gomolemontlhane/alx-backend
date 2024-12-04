import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((job) => {
        const notificationJob = queue.create('push_notification_code_3', job);

        notificationJob.save((err) => {
            if (err) {
                console.error('Failed to save the job:', err);
                return;
            }
            console.log(`Notification job created: ${notificationJob.id}`);
        });

        notificationJob.on('complete', () => {
            console.log(`Notification job ${notificationJob.id} completed`);
        }).on('failed', (err) => {
            console.log(`Notification job ${notificationJob.id} failed: ${err}`);
        }).on('progress', (progress) => {
            console.log(`Notification job ${notificationJob.id} ${progress}% complete`);
        });
    });
}

export default createPushNotificationsJobs;
