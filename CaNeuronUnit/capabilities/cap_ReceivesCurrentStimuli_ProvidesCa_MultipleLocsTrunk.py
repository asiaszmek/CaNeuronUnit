from sciunit import Capability


class ReceivesCurrentStimuli_ProvidesCa_MultipleLocsTrunk(Capability):
    """
    Injected a square pulse of current in a section of the model.
    Provide Ca concentration or Ca-bound Ca indicator dye concentration
    in multiple locations.
    """

    def inj_cur_record_Ca_multiple_loc(self, amp, delay, dur, loc_stim,
                                       dend_locations):
        """
        This function needs to be implemented by the model.

        This function must return numpy arrays containing the time vector 
        and the voltage values recorded in the stimulus location, and 
        a nested dictionary containing concentration vectors in specified 
        dendritic locations at the distances in this test examined.

        Parameters
        ----------
        amp: float
             amplitude of the injected current (nA)
        delay: float
             interval between the beginning of the simulation and the beginning
             of the stimulation (ms)
        duration: float
             duration of the current injection (ms)
        loc_stim: NEURON seg (or possibly in the future Moose seg)
             stimulation location
        dend_locations: list of recording locations in the form:  
             dend_loc = (dist1, ['trunk_segment1_1', location], 
                                ['trunk_segment1_2', location]),
                        (dist2, ['trunk_segment2', location]),
                        (dist3, ['trunk_segment3', location]), 
                        (dist4, ['trunk_segment4', location])
        """
        raise NotImplementedError()

    def get_multiple_conc(self, amp, delay, dur, loc_stim, dend_locations):
        """
        Called by the test function. Calls inj_cur_record_Ca_multiple_loc 
        function.
        """
         t, i_stim, conc = self.inj_cur_record_Ca_multiple_loc(amp, delay, dur,
                                                               loc_stim,
                                                               dend_locations)
        return t, i_stim, conc
