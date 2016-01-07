import requests


XC_BASE_URL = 'http://www.xeno-canto.org/api/2/recordings'
XC_QUERY_URL = XC_BASE_URL + '?query='
STEP_SIZE = 10


def query_xc(query_url):
    """ Make the query and return the results

    :param query_url:
    :return:
    """
    r = requests.get(query_url)
    return r.json()


def download_archive(first_nr=1, last_nr=None):
    """ Function to (gradually) download the whole archive of audio recordings, in sequential order of id's

    :param first_nr: by default, start with recording id=1
    :param last_nr: by default, automatically determine what the last recording id is
    :return:
    """
    # Get nr of last recording in the archive
    if not last_nr:
        last_rec = get_last_recording()
        if not last_rec:
            # Return error here, unable to find last recording
            return None
        last_nr = int(last_rec.get('id'))

    # Loop and download sets of recordings according to the step size
    for idx in range(first_nr, last_nr, STEP_SIZE):
        # Query for recordings in an nr range
        recs = query_nr_range(idx, idx+STEP_SIZE-1)

        # Process recordings
        pass


def query_since(since=0):
    """ Function to query the recordings that have been uploaded in the last day(s)

    :param since:
    :return:
    """
    # Form the query url
    query_url = XC_QUERY_URL + 'since:%d' % since

    return query_xc(query_url)


def query_nr_range(first_nr, last_nr):
    """ Function to query the recordings within an nr range

    :param first_nr:
    :param last_nr:
    :return:
    """
    # Form the query url
    query_url = XC_QUERY_URL + 'nr:%d-%d' % (first_nr, last_nr)

    return query_xc(query_url)


def get_last_recording():
    """ Get the last recording that was added to the api

    :return:
    """
    last_rec = None
    since = 0
    got_recording = False
    while not got_recording:
        # Get the latest recordings
        latest_recs = query_since(since=since)
        if latest_recs.get("recordings"):
            # Find the biggest nr number in the group, which is the last recording that was added
            last_rec = sorted(latest_recs.get('recordings'), key=lambda k: k['id'])[-1]
            got_recording = True
        else:
            since += 1

    return last_rec


download_archive()

