% MATLAB Code for Ch11 Lab 1

function ExtendedToneReactionTest()
    InitializePsychSound(1);

    frequencies = [500, 1000, 2500, 5000, 7500, 10000];  
    decibels = [30, 50, 70];
    duration = 1; 
    samplingRate = 44100; 
    nrchannels = 2; 

    responses = zeros(length(frequencies), length(decibels));

    pahandle = PsychPortAudio('Open', [], [], 0, samplingRate, nrchannels);

    for freqIdx = 1:length(frequencies)
        freq = frequencies(freqIdx);
        t = linspace(0, duration, samplingRate * duration);
        beepSound = sin(2 * pi * freq * t);
        beepSound = [beepSound; beepSound];

        for dbIdx = 1:length(decibels)
            dbLevel = decibels(dbIdx);
            amplitude = 10^((dbLevel - 94) / 20);
            testSound = beepSound * amplitude;

            PsychPortAudio('FillBuffer', pahandle, testSound);
            
            disp(['Testing frequency: ' num2str(freq) ' Hz at ' num2str(dbLevel) ' dB. Get ready...']);
            WaitSecs(2);  
            PsychPortAudio('Start', pahandle, 1, 0, 1);
            baseTime = GetSecs;
            
            KbQueueCreate;
            KbQueueStart;
            KbQueueFlush;

            disp('Listening for keypress...');
            startTime = GetSecs;
            while GetSecs - startTime < 5 
                [pressed, firstPress] = KbQueueCheck;
                if pressed
                    responses(freqIdx, dbIdx) = 1;
                    fprintf('Response at %d Hz, %d dB.\n', freq, dbLevel);
                    break;
                end
            end

            if ~pressed
                responses(freqIdx, dbIdx) = 0;
                disp('No response during this test.');
            end

            KbQueueStop;
            KbQueueRelease;
            PsychPortAudio('Stop', pahandle);
        end
    end

    PsychPortAudio('Close', pahandle);  

    figure;
    hold on;
    for dbIdx = 1:length(decibels)
        for freqIdx = 1:length(frequencies)
            if responses(freqIdx, dbIdx) == 1
                plot(frequencies(freqIdx), dbIdx, 'o', 'Color', 'g', 'MarkerFaceColor', 'g', 'MarkerSize', 8);  
            else
                plot(frequencies(freqIdx), dbIdx, 'x', 'Color', 'r', 'MarkerSize', 10);  
            end
        end
    end
    xlabel('Frequency (Hz)');
    ylabel('Decibel Level');
    xticks(frequencies);
    yticks(1:length(decibels));
    yticklabels(arrayfun(@(d) [num2str(d) ' dB'], decibels, 'UniformOutput', false));
    title('Frequency Response Test Results');

    h1 = plot(NaN, NaN, 'og', 'MarkerFaceColor', 'g', 'MarkerSize', 8);  
    h2 = plot(NaN, NaN, 'xr', 'MarkerSize', 10);  
    legend([h1, h2], {'Response', 'No Response'}, 'Location', 'best');

    grid on;
    hold off;
end
